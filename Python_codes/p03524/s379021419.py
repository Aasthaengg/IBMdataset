# babacccabab a4 b4 c3
# a bc a bc a bc a b
# bがひとつ少なくても、cがひとつ多くてもよさそう
# bがひとつ多い場合(a4 b5 c3)は無理そう
# なので登場するやつのminとmaxの差でいけそう
# と思ったらサンプル2の場合があるので、2種類しかない場合は基本的に無理そう
# ただし1文字だけしか無い場合はいけそう

# -> なんか1つだけWAなる
# -> よくよく考えたら ab みたいな場合はおｋだわ たぶんこれにひっかっかた
s = input()
if len(s) == 1:
    print("YES")
    exit()
abc = [s.count("a"), s.count("b"), s.count("c")]
if len(s) == 2 and max(abc) == 1:
    print("YES")
    exit()
if 0 in abc:
    print("NO")
else:
    print("YES" if max(abc) - min(abc) < 2 else "NO")