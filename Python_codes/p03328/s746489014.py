a,b = map(int,input().split(" "))
diff = b-a
t_b = (diff+1)*diff/2
print(int(t_b-b))