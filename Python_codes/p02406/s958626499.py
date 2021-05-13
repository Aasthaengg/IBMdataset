n = int(input())
num_list = [i for i in range(1,n+1)]
num2_list = [i for i in num_list if i%3==0]#3で割り切れる値
list_str = [s for s in map(str,num_list) if '3' in s]#3が含まれる場合
list_in = list(map(int,list_str))#list変換
list_uniq = list(set(num2_list+list_in))
list_uniq.sort()
print(' '+' '.join(str(i) for i in list_uniq))

