N = int(input())
A = list(map(int,input().split()))
cnt_eve = 0
for a in A:
  if a%2 == 0:cnt_eve += 1
print(3**N-(2**cnt_eve))