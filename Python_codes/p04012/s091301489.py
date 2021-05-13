w=input()
W=len(w)

for i in range(W):
    if w.count(w[i])%2==0:
        if i==W-1:
            print("Yes")
            break
  
    else:
        print("No")
        break


