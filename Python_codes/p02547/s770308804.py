def func(D):
  comb = 0
  for item in D:
    if item[0]==item[1]:
      comb+=1
    else:
      comb=0
    
    if comb==3:
      return "Yes"  
  return "No"

if __name__ == "__main__":
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    print(func(D))