s = input()
n = len(s)
ac = ["A","C","G","T"]
acgt = []
for i in range(n+1):
    for j in range(i+1,n+1):
        #print(s[i:j])

        a = list(set(list(s[i:j])))
        for k in range(len(a)):
            if a[k] not in ac:
                break
        else:
            #acgt += [s[i:j]]
            #print(f"○{s[i:j]}")
            acgt += [len(s[i:j])]    

if acgt == []:
    acgt += [0]

print(max(acgt))