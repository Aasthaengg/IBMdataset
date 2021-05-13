import re
s=input()
result=re.fullmatch(r'(\d{3})(\d)/(\d{2})/(\d{2})',s)
print(result.group(1)+'8/'+result.group(3)+'/'+result.group(4))