S = input()
w = int(input())

result =""
for i in range(0,len(S),w):
  result = result + S[i]
print(result)