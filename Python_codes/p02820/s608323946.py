N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
score = {"r":P, "s":R, "p":S} 
m = {"r":"p", "s":"r", "p":"s"}
command= []
mm = []
ans = 0


for i, t in enumerate(T):
    if t == "r":
      c = "p"
      point = P
    elif t == "s":
      c ="r" 
      point = R
    elif t == "p":
      c = "s"
      point = S
    
    if (i - K >= 0) and (command[i - K] == c):
        c = ""
        point = 0
    
    ans += point
    command.append(c)
print(ans)