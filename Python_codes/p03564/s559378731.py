n = int(input())
k = int(input())

def re_def(num, c, n=n, k=k):
    if c==n:
        return num
    for i in range(2):
        if i==0:
            num1 = re_def(num*2, c+1)
        else:
            num2 = re_def(num+k, c+1)
    return min([num1, num2])
print(re_def(1,0))