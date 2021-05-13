K , S = map(int,input().split())
k = 0
for i in range(K+1):
  for j in range(min([S-i+1,K+1])):
    if 0 <= S - i - j <= K:
      k += 1
print(k)      