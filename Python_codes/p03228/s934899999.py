A,B,K=map(int, input().split())
List = [A,B]
for i in range(K):
  if(List[i]%2==1):
    List[i]=(List[i]-1)//2
    List[i+1]=List[i+1]+List[i]
    List.append(List[i])
  else:
    List[i]=(List[i])//2
    List[i+1]=List[i+1]+List[i]
    List.append(List[i])
#print(List[-3],List[-2])
if(K%2==1):
  print(List[-1],List[-2])
else:
  print(List[-2],List[-1])