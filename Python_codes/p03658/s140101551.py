a,b = map(int,input().split())
num = list(map(int,input().split()))   
num.sort()
num=num[-b:]

print(sum(num))