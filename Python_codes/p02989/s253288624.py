N = int(input())
number = list(map(int,input().split()))
number.sort(reverse=True)
a = int((N/2)-1)
b = int(N/2)
print(number[a]-number[b])