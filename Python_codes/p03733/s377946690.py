N, T = map(int,input().split())
List = list(map(int,input().split()))
Data = [0,0]
for item in List:
  if Data[0]>=item:
    Data[1] += T + item -Data[0]
    Data[0] = item +T
  else:
    Data[1] += T
    Data[0] = item +T
print(Data[1])