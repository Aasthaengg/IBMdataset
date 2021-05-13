A,B,M=map(int, input().split())
As=list(map(int, input().split()))
Bs=list(map(int, input().split()))
List=[]
for i in range(M):
  List.append(list(map(int, input().split())))

ans=min(As)+min(Bs)
for l in List:
  candidate=As[l[0]-1]+Bs[l[1]-1]-l[2]
  ans = min(ans, candidate)
print(ans)
