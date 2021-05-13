instring = input()
head_str = ""
foot_str = ""
ans_str = ""
ref = "keyence"
ref_rev = ref[::-1]
flag = False

# 頭からあっているかチェックしていく
start_index = 0
end_index = len(ref)-1
# 前から数えていく
for i in range(len(instring)):
    head_str += instring[i]
    now_ref = ref[:(i+1)]
    # 前から並べたときに一致しているかチェック
    if(head_str != now_ref):
        # どこで一致しなくなったかメモ
        start_index = i
        flag = True
        break

# normal
if(flag):
    ans_str += head_str[:start_index]
else:
    ans_str = head_str

end_flag = False
# 既に一致していたらこれ以上やらない
if(ans_str == ref):
    print("YES")
    end_flag = True

ans_len = len(ans_str)    

# 後ろから数えていく
for i in range(len(ref)-ans_len):        
    foot_str += instring[-(i+1)]
    now_ref = ref_rev[:(i+1)]
    if (foot_str != now_ref):
        end_index = i
        break

# 反転させる
foot_str = foot_str[:end_index][::-1] 
ans_str += foot_str

if(end_flag != True):
    if(ans_str == ref):
        print("YES")
    else:
        print("NO")