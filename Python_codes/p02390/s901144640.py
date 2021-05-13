x = int(input())
h = x //3600
m = (x-(h*3600))//60
s= (x-(h*3600))%60
print("{}:{}:{}".format(h,m,s))
