N = int(input())
V = list(map(int,input().split()))

import collections

if len(set(V)) == 1:
  print(N//2)
else:
  evens = [V[n] for n in range(0,N,2)]
  odds = [V[n] for n in range(1,N,2)]
  
  c_evens = collections.Counter(evens).most_common()
  c_odds = collections.Counter(odds).most_common()
  
  mode_in_evens = c_evens[0][0]
  mode_number_in_evens = c_evens[0][1]
  
  mode_in_odds = c_odds[0][0]
  mode_number_in_odds = c_odds[0][1]
  
  ans = N - (mode_number_in_evens+mode_number_in_odds)
  
  if mode_in_evens == mode_in_odds:
    if len(c_evens) != 1:
      second_mode_number_in_evens = c_evens[1][1]
    else:
      second_mode_number_in_evens = 0
    ans_candidate_1 = N - (second_mode_number_in_evens+mode_number_in_odds)      
      
    if len(c_odds) != 1:
      second_mode_number_in_odds = c_odds[1][1]
    else:
      second_mode_number_in_odds = 0
    ans_candidate_2 = N - (mode_number_in_evens+second_mode_number_in_odds) 
    
    ans = min(ans_candidate_1,ans_candidate_2)
    
  print(ans)