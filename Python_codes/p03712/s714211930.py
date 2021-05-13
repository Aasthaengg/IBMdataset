h,w=map(int,input().split())
a=[list(input().split()) for _ in range(h)]

print('#'*(w+2))
for j in a:
	print('#'+str(*j)+'#')
print('#'*(w+2))