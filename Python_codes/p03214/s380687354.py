N = int(input())
List = list(map(int,input().split()))
mean = sum(List)/N
diff = [abs(i -mean) for i in List]

for i,item in enumerate(diff):
  if item == min(diff):
    Answer = i
    break
print(Answer)