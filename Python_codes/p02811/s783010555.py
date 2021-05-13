k, x = map(int, input().split())

ret = "No"
if k * 500 >= x:
    ret = "Yes"

print("{}".format(ret))