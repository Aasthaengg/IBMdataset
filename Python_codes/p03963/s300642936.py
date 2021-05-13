a = list(map(int,input().split()))

if a[0] == 1:
  answer = a[1];
else:
  answer = a[1]*(a[1]-1)**(a[0]-1)

print(answer)