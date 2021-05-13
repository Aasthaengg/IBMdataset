#!/usr/bin/python
 
input_data = list(map(int,input().split()))
 
neko = input_data[0]
neko_inu = input_data[1]
d = input_data[2]
 
if neko > d:
    print("NO")
elif neko+neko_inu < d:
    print("NO")
else:
    print("YES")