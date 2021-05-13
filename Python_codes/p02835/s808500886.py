a, b, c, = map(int, input().split())

ret = "bust"
if a + b + c <= 21:
   ret = "win" 

print("{}".format(ret))