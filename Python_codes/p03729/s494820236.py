import sys

if sys.platform =='ios':
    sys.stdin=open('input_file.txt')
    

s1,s2,s3=map(str,input().split())

if s1[-1]==s2[0] and s2[-1]==s3[0]:
	print("YES")
else:
	print("NO")