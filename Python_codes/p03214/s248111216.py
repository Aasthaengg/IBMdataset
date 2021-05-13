n = int(input())
a = list(map(int, input().split()))
num = sum(a)/n
a = [abs(i-num) for i in a]
print(a.index(sorted(a)[0]))


    
