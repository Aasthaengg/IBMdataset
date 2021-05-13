# -*- coding: utf-8 -*-

def input_converter(key_string):
    key_string = key_string.replace('A', '1')
    key_string = key_string.replace('T', '2')
    key_string = key_string.replace('C', '3')
    key_string = key_string.replace('G', '4')
    return int(key_string)


class HashTable(object):
    def __init__(self, hash_size = 2 ** 26):
        self.hash_size = hash_size
        self.hash_array = [None] * self.hash_size

    def insert_value(self, data, key):
        collision_number = 0
        next_index = self.hash_function(key, collision_number)
        while self.hash_array[next_index] is not None:
            collision_number += 1
            next_index = self.hash_function(key, collision_number)
        # print self.hash_array[next_index]
        self.hash_array[next_index] = data

    def search_value(self, data, key):
        collision_number = 0
        next_index = self.hash_function(key, collision_number)
        next_data = self.hash_array[next_index]
        while True:
            if (next_data is None) or (collision_number > self.hash_size):
                return False
            elif next_data == data:
                return True
            else:            
                collision_number +=1
                next_index = self.hash_function(key, collision_number)
                next_data = self.hash_array[next_index]

    def hash_function(self, key, collision_number):
        def h1(key):
            return key % self.hash_size
    
        def h2(key):
            return key % (self.hash_size - 1)

        return (h1(key) + collision_number * h2(key)) % self.hash_size


def main():
    input_size = int(raw_input())
    hash_table = HashTable()
    counter = 0
    while counter < input_size:
        command, key = raw_input().split(' ')
        if command == 'insert':
            hash_table.insert_value(key, input_converter(key))
        else:
            if hash_table.search_value(key, input_converter(key)):
                print 'yes'
            else:
                print 'no'
        counter += 1


if __name__ == '__main__':
    main()