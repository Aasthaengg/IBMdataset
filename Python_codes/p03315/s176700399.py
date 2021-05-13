S=str(input())
strings="+","-"
sum=0
for i in range(4):
    if S[i]=="+":
        sum += 1
    else:
        sum -= 1
print(sum)