import re
S=input()
print("NYoe s"[len(re.sub("[RUD]",'',S[0::2]))==0==len(re.sub("[LUD]",'',S[1::2]))::2])