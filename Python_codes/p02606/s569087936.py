l, r, d = map(int,input().rstrip("\n").split(" "))
 
answer = (r // d) - ((l-1) // d)
 
print(answer)