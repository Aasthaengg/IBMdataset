import fractions
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

class Counter:
    def __init__(self):
        self.dict = {}

    def add(self,x):
        if x in self.dict: self.dict[x] += 1
        else: self.dict[x] = 1

    def decrement(self,x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict


INF=10**20
def main():
    K=ii()

    ans = 0
    
    counter = Counter()

    for a in range(1,K+1):
        for b in range(1,K+1):
                x = fractions.gcd(a,b)
                counter.add(x)

    count = counter.get_dict()
    for c in range(1,K+1):
        for key in count.keys():
            val = count[key]
            x = fractions.gcd(key,c)
            ans += val * x



    print(ans)



if __name__ == "__main__":
    main()