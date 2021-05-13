S = input()
topping = 0 #トッピング料金変数を初期化
#oが何文字あるか数えて、その文字数×１００がトッピング料金

for i in S:
    if i == "o":
        topping = topping + 1 
#print(topping)        
price = 700 +  100*topping
print(price)