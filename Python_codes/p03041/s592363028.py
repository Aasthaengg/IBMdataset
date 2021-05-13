N, K = map(int, input().split())
s3 =[]

s = list(input())

s1 = s


s2= s1[K-1]

s3 = s2.lower()

s1[K-1] = s3

print('' .join(s1))