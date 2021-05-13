n = int(input())
s1 = int(n * (n+1)/2)
s2 = int(n//3 * (n//3 + 1) * 3/2)
s3 = int(n//5 * (n//5 + 1) * 5/2)
s4 = int(n//15 * (n//15 + 1) * 15/2)
 
print(s1 - s2 - s3 + s4)