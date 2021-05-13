k = int(input())
s = str(input())
add_str = "..."

print(s if len(s) <= k else s[0:k]+add_str)