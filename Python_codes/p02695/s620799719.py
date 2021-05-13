# -*- coding: utf-8 -*-

class Combination_with_repetition():
    def getPattern(self, arr :list, r :int) -> list:
        self._selected=[]
        self._all_pattern=[]
        
        self._make(arr,r)
        return self._all_pattern
        
    def _make(self, arr :list, r :int):
        if r == 0:
            self._all_pattern.append(self._selected[:])
            return 
        
        for i in range(len(arr)):
            self._selected.append( arr[i] )
            self._make(arr[i:],r-1)
            
            self._selected.pop()  # Backtracking

#-----
N,M,Q = list(map(int, input().rstrip().split()))
abcd_list = [list(map(int, input().rstrip().split())) for i in range(Q)]

#-----
comb_rep = Combination_with_repetition()
pattern = comb_rep.getPattern( list(range(1, M+1)) , N)


max_sum = 0

for pat in pattern:
    tmp_sum = 0
    
    for a,b,c,d in abcd_list:
        if ( pat[b-1] - pat[a-1] ) == c:
            tmp_sum += d
    
    max_sum = max(max_sum, tmp_sum)

print(max_sum)
