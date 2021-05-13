dic = {"a":0,"b":25,"c":24,"d":23,"e":22,"f":21,"g":20,"h":19,"i":18,"j":17,"k":16,"l":15,"m":14,"n":13,"o":12,"p":11,"q":10,"r":9,"s":8,"t":7,"u":6,"v":5,"w":4,"x":3,"y":2,"z":1}
ls = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

s = input()
k = int(input())
s_l = []
for i in range(len(s)):
    s_l.append(s[i])

for i in range(len(s_l)):
    if dic[s_l[i]] <= k:
        k -= dic[s_l[i]]
        s_l[i] = "a"

if k > 0:
    s_l[-1] = ls[((26 - dic[s_l[-1]]) + k)%26]

for i in range(len(s_l)):
    print(s_l[i],end = "")
print()
