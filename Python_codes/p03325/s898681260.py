def div(k):
    k = int(k)
    i = 0
    while k%2==0:
        k//=2
        i+=1
    return i
n = int(input());print(sum(list(map(div, input().split()))))