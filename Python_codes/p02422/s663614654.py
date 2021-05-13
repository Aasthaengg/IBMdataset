s = input()
n = int(input())

s = list(s)

for i in range(n):
  arv = [a for a in input().split()]

  if (arv[0] == "reverse"):
    reverse_s = s[int(arv[1]) : int(arv[2])+1]
    reverse_s.reverse()
    s[int(arv[1]) : int(arv[2])+1]= reverse_s
  
  if (arv[0] == "replace"):
    s[int(arv[1]) : int(arv[2])+1] = list(arv[3])
        
  if (arv[0] == "print"):
    print("".join(s[int(arv[1]):int(arv[2])+1]))
