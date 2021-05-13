s = list(input())

if len(s) >= 9 and "".join(s) != "AKIHABARA":
    print("NO")
elif "".join(s) == "AKIHABARA":
    print("YES")
else:
    for i in range(2**(len(s)+1)):
        lst = [""]*50
        for j in range(len(s)+1):
            if i&(1<<j):
                lst[j] = "A"
        #print(lst)
        
        result = ""               
        for k1,k2 in zip(lst,s+["",""]):
            result += k1+k2
        #print(result)
        if result == "AKIHABARA":
            print("YES")
            exit()
        else:
            continue
    else:
        print("NO")