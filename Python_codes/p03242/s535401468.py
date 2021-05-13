dic = {"1":"9","9":"1"}
n = list(input())
for i in range(0,3,1):
    n[i]=dic[n[i]]
print("".join(n))