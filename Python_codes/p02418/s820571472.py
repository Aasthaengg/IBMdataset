def judg_unit(ss,pp):
    sss = ss + ss + ss
    result = sss.find(pp)
    if result != -1:
        return "Yes"
    else :
        return "No"

s = str(input())
p = str(input())
print(judg_unit(s,p))

