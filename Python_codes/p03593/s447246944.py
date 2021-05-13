import bisect

h, w = map(int, input().split())
figure_dic = {}
def add_dic(figure):
    if not figure in figure_dic:
        figure_dic[figure] = 0
    figure_dic[figure] += 1
for i in range(h):
    line = list(input())
    for j in line:
        add_dic(j)
figures = []
for key, items in figure_dic.items():
    figures.append(items)
figures.sort()
same_boxes = []
if h % 2 == 0:
    if w % 2 == 0:
        same_boxes += [4 for i in range(h*w//4)]
    else:
        same_boxes += [4 for i in range((w//2)*(h//2))]
        same_boxes += [2 for i in range(h//2)]
else:
    if w % 2 == 0:
        same_boxes += [4 for i in range((h//2)*(w//2))]
        same_boxes += [2 for i in range(w//2)]
    else:
        same_boxes += [4 for i in range((h//2)*(w//2))]
        same_boxes += [2 for i in range(h//2 + w//2)]
        same_boxes += [1]
same_boxes.sort(reverse=True)
l = len(figures)
flag = 0
for box in same_boxes:
    left = bisect.bisect_left(figures, box)
    if left == l:
        flag = 1
        break
    figures[left] -= box
    figures.sort()
if flag:
    print("No")
else:
    print("Yes")