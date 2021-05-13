n = input()
nlen = len(n)
sum = 0
for i in range(nlen):
    sum += int(n[i])
if(sum % 9 == 0):
    print("Yes")
else:
    print("No")
