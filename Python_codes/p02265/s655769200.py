# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_C&lang=jp
sample_input = list(range(3))
sample_input[0] = '''7
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5'''
sample_input[1] = '''9
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
deleteFirst
deleteLast'''
sample_input[2] = '''8
insert 1000000000
insert 999999999
deleteLast
insert 1234566890
insert 5
deleteFirst
insert 7
delete 5'''
give_sample_input = None
if give_sample_input is not None:
    sample_input_list = sample_input[give_sample_input].split('\n')
    def input():
        return sample_input_list.pop(0)
        
# main
from collections import deque

num_of_command = int(input())
doubly_list = deque()
for n in range(num_of_command):
    str_command = input()
    if str_command == 'deleteFirst':
        doubly_list.popleft()
        continue
    elif str_command == 'deleteLast':
        doubly_list.pop()
        continue
    command_name = str_command.split()[0]
    command_obj = int(str_command.split()[1])
    if command_name == 'insert':
        doubly_list.appendleft(command_obj)
    elif command_name == 'delete':
        try:
            doubly_list.remove(command_obj)
        except ValueError:
            continue

output = ''
for item in doubly_list:
    output += str(item) + ' '
output = output.rstrip()
print(output)