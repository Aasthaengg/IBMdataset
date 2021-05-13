def main():
  n = int(input())
  xy = [map(str, input().split()) for _ in range(n)]
  x, y = [list(i) for i in zip(*xy)]
  ans_list=list(range(0,n))
  for i in range(0,n):
    min=i
    for j in range(i+1,n):
      if x[ans_list[min]]>x[ans_list[j]] or (x[ans_list[min]]==x[ans_list[j]] and int(y[ans_list[min]])<int(y[ans_list[j]])):
        min=j
    
    if ans_list[min]!=ans_list[i]:
      tmp=ans_list[i]
      ans_list[i]=ans_list[min]
      ans_list[min]=tmp
    print(ans_list[i]+1)
  
main()