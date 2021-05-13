# 1度`BC`を`D`に置き換えて操作を考える
S = input()

new_s = ""
pointa = 0
while pointa != len(S):
    if pointa == len(S) - 1:
        new_s += S[pointa]
        break
    if S[pointa] == "B" and S[pointa+1] == "C":
        new_s += "D"
        pointa += 2
    else:
        new_s += S[pointa]
        pointa += 1

# Dが出現した時、その直前に存在するAの回数だけ操作を行うことができる
count = 0
ans = 0
for i in range(len(new_s)):
    if new_s[i] == "D":
        ans += count
    elif new_s[i] == "A":
        count += 1
    else:
        count = 0
print(ans)
