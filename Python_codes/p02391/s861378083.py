a,b=map(int,input().split())
sign="=="
if a<b:sign="<"
if a>b:sign=">"
print("a",sign,"b")