# from pprint import pprint
# import math
# import collections

# n = int(input())
s = input()
# s = 'keyxxxxxxxxxxence'
# n, k = map(int, input().split(' '))
# a = list(map(int, input().split(' ')))

K = 'keyence'

for i in range(len(s)):
    for j in range(len(s)):
        s1 = s[0:i]
        s2 = s[i:i + j]
        s3 = s[i + j:]

        # print(s1,s2,s3)
        if s1 == K or s2 == K or s3 == K or s1 + s2 == K or s1 + s3 == K or s2 + s3 == K:
            print('YES')
            exit()

print('NO')
