
class Stack:
    def __init__(self, data=None):
        # Pythonではクラスのデフォルト引数は１度しか初期化されないため、
        # うっかりdata=[]としてしまうと、複数のインスタンスを生成したときに
        # 同じ配列を参照することになってしまう！！！
        # http://amacbee.hatenablog.com/entry/2016/12/07/004510
        if data is None:
            self.data = []
        else:
            self.data = data

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty() is True:
            return None
        else:
            return self.data.pop(-1)

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def get_length(self):
        return len(self.data)

    def reverse(self):
        self.data.reverse()


# \\//
# \\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\

diagram = input()
A = 0  # 総面積
k = 0  # 水たまりの数
L = []  # 各水たまりの面積

s1 = Stack()
s2 = Stack()

new_flood = False

# s1.push(10)
# s1.push(20)
# s1.push(30)
# print(s2.data)

for i, vector in enumerate(diagram):
    # print('----------')
    # print(i, vector)

    if vector == '\\':
        # print('下り')
        # print('test')
        s1.push(i)

        # 個別
        # data = {'first_pos': i, 'area': 0}
        # s2.push(data)
        # grad = 'down'

        new_flood = True

    elif vector == '/':
        # print('上り')
        j = s1.pop()
        if j is not None:
            # print(i, j)
            A += i - j

            # current_flood = s2.pop()
            # if current_flood['first_pos'] =
            # Agenshidan88
            # = i:
            #     current_flood['area'] += i - j

            size = i - j

            if new_flood is True:
                s2.push({'first_pos': j, 'size': size})
                new_flood = False

            # if s2.is_empty() is True:
            #     s2.push({'first_pos': j, 'area': i-j})

            else:
                current_flood = s2.pop()
                current_flood['first_pos'] = j
                current_flood['size'] += size

                while True:
                    prev_flood = s2.pop()
                    if prev_flood is not None:
                        if prev_flood['first_pos'] > j:
                            current_flood['size'] += prev_flood['size']
                        else:
                            s2.push(prev_flood)
                            s2.push(current_flood)
                            break
                    else:
                        s2.push(current_flood)
                        break

    # print(s1.data)
    # print(s2.data)
    # print('----------')

print(A)

output = str(s2.get_length())
for elem in s2.data:
    output += ' ' + str(elem['size'])

print(output)

