class SegmentTree:
    def __init__(self,orig,func,unit):
        _len= len(orig)
        self.func = func
        self.size = 1 << (_len-1).bit_length()
        self.tree = [unit] * self.size + orig + [unit] *(self.size-_len)
        self.unit = unit
        
        for i in range(self.size -1,0,-1):
            self.tree[i] = func(self.tree[i*2], self.tree[i*2+1])
            
    def update(self, i, v):
        i+=self.size
        self.tree[i] = v
        while i:
            i//=2
            self.tree[i]=self.func(self.tree[i*2],self.tree[i*2+1])
    
    def find(self,l,r):
        l+=self.size
        r+=self.size
        ret=self.unit
        while l<r:
            if l&1:
                ret = self.func(ret,self.tree[l])
                l+=1
            if r&1:
                r-=1
                ret=self.func(ret,self.tree[r])
            l//=2
            r//=2
        return ret
      
import sys
input = sys.stdin.readline
from operator import or_

input()
seg = SegmentTree([1 << ord(x) - 97 for x in input()[:-1]], or_, 0)
ans = []
for _ in range(int(input())):
  f, x, y = input().split()
  if f == "1":
    seg.update(int(x) - 1, 1 << ord(y) - 97)
  else:
    ans.append(bin(seg.find(int(x) - 1, int(y))).count("1"))
print(*ans)