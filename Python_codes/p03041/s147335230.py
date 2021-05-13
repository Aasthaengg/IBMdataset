a,b = input().split(" ")
c = list(map(str,input().split()))
print(c[0][:int(b)-1] + c[0][int(b)-1].lower() + c[0][int(b):])