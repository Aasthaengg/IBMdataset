n=int(input())
a=['a','b','c','d','e','f','g','h','i','j']

def dfs(s, count):
    if len(s) == n:
        print(s)
        return
 
    for z in range(count + 1):
        dfs(s + a[z], count + 1 if z == count else count)

dfs("",0) 
